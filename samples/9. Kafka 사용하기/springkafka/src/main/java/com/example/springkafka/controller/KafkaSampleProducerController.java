package com.example.springkafka.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.example.springkafka.service.KafkaSampleProducerService;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@RestController
public class KafkaSampleProducerController {
    
    @Autowired
    private KafkaSampleProducerService kafkaSampleProducerService;

    @GetMapping("/send/{message}")
    public String sendMessage(@PathVariable("message") String message) {
        log.info("[KafkaSampleProducerController][sendMessage] Start");
        kafkaSampleProducerService.sendMessage(message);
        return "성공";
    }
}
