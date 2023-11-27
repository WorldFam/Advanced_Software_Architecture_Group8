package com.example.supply;

import org.springframework.stereotype.Service;

import javax.naming.InsufficientResourcesException;
import java.math.BigInteger;
import java.util.List;

@Service
public class SupplyService {
    private final SupplyRepository supplyRepository;

    public SupplyService(SupplyRepository supplyRepository){
        this.supplyRepository = supplyRepository;
    }

    public List<ResourceEntity> fetchResource(){
        return (List<ResourceEntity>) supplyRepository.findAll();
    }

    public void addResource(Resource resource){
        if(supplyRepository.existsBySize(resource.size())){
            throw new IllegalArgumentException("Resource with this size already exists");
        }

        ResourceEntity entity = new ResourceEntity();
        entity.setSize(resource.size());
        entity.setAmount(BigInteger.valueOf(resource.amount()));
        supplyRepository.save(entity);
    }

    public void updateResource(String id, String amount){
        long parsedAmount = Long.parseLong(amount);
        if (parsedAmount < 0) {
            throw new IllegalArgumentException("Amount must be non-negative");
        }

        ResourceEntity entity = supplyRepository.findById(Long.valueOf(id)).orElseThrow(() -> new IllegalArgumentException("Resource does not exists"));
        entity.setAmount(entity.getAmount().add(BigInteger.valueOf(parsedAmount)));
        supplyRepository.save(entity);
    }

    public void supplyWithResource(Resource resource) throws InsufficientResourcesException {
        if (resource.amount() == 0) {
            return;
        }
        
        ResourceEntity entity = supplyRepository.findBySize(resource.size());

        BigInteger amount = BigInteger.valueOf(resource.amount());

        if (amount.compareTo(entity.getAmount()) > 0) {
            throw new InsufficientResourcesException();
        }

        BigInteger remainingAmount = entity.getAmount().subtract(amount);

        entity.setAmount(remainingAmount);
        supplyRepository.save(entity);
    }


}
