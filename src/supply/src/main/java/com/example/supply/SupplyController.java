package com.example.supply;

import lombok.AllArgsConstructor;
import lombok.NonNull;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;

import javax.naming.InsufficientResourcesException;
import java.util.List;

@RestController
@AllArgsConstructor
public class SupplyController {

    private final SupplyService supplyService;

    @GetMapping(value = "/resource", produces = MediaType.APPLICATION_JSON_VALUE)
    public List<ResourceEntity> fetchResource() {
        return supplyService.fetchResource();
    }

    @PostMapping(value = "/resource", consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Void> addResource(@RequestBody Resource resource) {
        supplyService.addResource(resource);
        return new ResponseEntity<>(HttpStatus.OK);
    }

    @PutMapping(value = "/resource/{id}", consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Void> updateResource(@PathVariable @NonNull String id, @RequestParam(name = "amount") String amount) {
        supplyService.updateResource(id, amount);
        return new ResponseEntity<>(HttpStatus.OK);
    }

    @PostMapping(value = "/supply", consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Void> supplyWithResource(@RequestBody Resource resource) throws InsufficientResourcesException {
        supplyService.supplyWithResource(resource);
        return new ResponseEntity<>(HttpStatus.OK);
    }

}
