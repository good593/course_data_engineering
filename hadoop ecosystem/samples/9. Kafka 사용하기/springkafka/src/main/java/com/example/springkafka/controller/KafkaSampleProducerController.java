package com.example.springkafka.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.example.springkafka.service.KafkaSampleProducerService;

@RestController
public class KafkaSampleProducerController {
    
    @Autowired
    private KafkaSampleProducerService kafkaSampleProducerService;

    @GetMapping("/send/{message}")
    public String sendMessage(@PathVariable String message) {
        kafkaSampleProducerService.sendMessage(message);
        return "성공";
    }
}
