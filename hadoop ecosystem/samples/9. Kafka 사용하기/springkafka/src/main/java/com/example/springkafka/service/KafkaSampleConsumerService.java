package com.example.springkafka.service;

import java.io.IOException;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@Service
public class KafkaSampleConsumerService {
    
    @KafkaListener(topics = "test", groupId = "group-id-oing")
    public void consume(String message) throws IOException {       

        log.info("[KafkaSampleConsumerService][consume] Start");
        log.info("receive message : "+message);
    }

}
