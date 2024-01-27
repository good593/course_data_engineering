
sudo apt-get -y update && \
sudo apt-get -y upgrade && \
sudo apt-get -y dist-upgrade && \
sudo apt-get install -y vim wget unzip ssh openssh-* net-tools chrony

sudo service ssh start
# ssh 실행 확인 
sudo systemctl status sshd

sudo hostnamectl set-hostname master
hostname

# chrony 확인 
sudo systemctl status chrony
vim /etc/chrony/chrony.conf
# 아래내용 수정 
server 203.248.240.140 iburst maxsources 2

sudo systemctl restart chrony
chronyc sources

sudo timedatectl set-timezone Asia/Seoul
date

sudo swapoff -a
sudo vim /etc/fstab

reboot

---
# Kubernetes 설치 (1.27)
## 설치전 작업 
- [IPv4를 포워딩하여 iptables가 브리지된 트래픽을 보게 하기](https://v1-27.docs.kubernetes.io/ko/docs/setup/production-environment/container-runtimes/)
```shell
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay && \
sudo modprobe br_netfilter

# 필요한 sysctl 파라미터를 설정하면, 재부팅 후에도 값이 유지된다.
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

# 재부팅하지 않고 sysctl 파라미터 적용하기
sudo sysctl --system
```

sudo apt-get install -y containerd
sudo systemctl status containerd.service
mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml

vim /etc/containerd/config.toml
# 아래내용 입력 
SystemdCgroup = true

systemctl restart containerd.service

---
## [1.27버전 설치](https://v1-27.docs.kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
sudo apt-get update
# apt-transport-https may be a dummy package; if so, you can skip that package
sudo apt-get install -y apt-transport-https ca-certificates curl

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.27/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.27/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update

apt-cache madison kubeadm
sudo apt-get install -y kubelet=1.27.10-1.1 kubeadm=1.27.10-1.1 kubectl=1.27.10-1.1

kubeadm init --apiserver-advertise-address 192.168.123.143 --pod-network-cidr=10.1.0.0/16

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

kubectl get no

### 아래는 worker들에게 
kubeadm join 192.168.123.143:6443 --token 4vizid.off62bxgyjg7dpc2 \
	--discovery-token-ca-cert-hash sha256:ab515439aca9781e6c636f26299a13932b05b773b84fb754b2e841a6b8661dff 

---
# [calico 설치](https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart) 
mkdir cni
cd cni

wget https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/tigera-operator.yaml
kubectl create -f tigera-operator.yaml

wget https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/custom-resources.yaml

vim custom-resources.yaml
# 수정 > pod-network-cidr=10.1.0.0/16

kubectl create -f custom-resources.yaml

kubectl get no
kubectl get ns
kubectl get all -n tigera-operator
kubectl get all -n calico-system
kubectl get all -n kube-system


# [kubectl autocomplete](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
cd ~
source <(kubectl completion bash) 
echo "source <(kubectl completion bash)" >> ~/.bashrc 
alias k=kubectl
complete -o default -F __start_kubectl k




--------
- https://youtu.be/Wr6nrBRqYYE?si=5-ipiwdFTRPsN1Jr











- https://medium.com/finda-tech/overview-8d169b2a54ff
- https://jazzy-laugh-6a8.notion.site/4-e1659fea4ae947569e7fa93aa30df51f
- https://github.com/237summit/k8s_core_labs



