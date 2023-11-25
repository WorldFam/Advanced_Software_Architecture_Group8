package supply.system;

import org.springframework.stereotype.Service;

import javax.naming.InsufficientResourcesException;
import java.math.BigInteger;

@Service
public class SupplyService {
    private final SupplyRepository supplyRepository;

    public SupplyService(SupplyRepository supplyRepository){
        this.supplyRepository = supplyRepository;
//        ResourceEntity small = new ResourceEntity();
//        small.setSize("0.5L");
//        small.setAmount(BigInteger.valueOf(1000));
//        supplyRepository.save(small);
//
//        ResourceEntity medium = new ResourceEntity();
//        medium.setSize("1.5L");
//        medium.setAmount(BigInteger.valueOf(1000));
//        supplyRepository.save(medium);
//
//        ResourceEntity large = new ResourceEntity();
//        large.setSize("2L");
//        large.setAmount(BigInteger.valueOf(17));
//        supplyRepository.save(large);
    }

    public void supply(Order order) throws InsufficientResourcesException {
        ResourceEntity entity = supplyRepository.findBySize(order.size());

        BigInteger amount = BigInteger.valueOf(order.amount());
        BigInteger remainingAmount = entity.getAmount().subtract(amount);

        if(remainingAmount.compareTo(BigInteger.ZERO) <= 0) {
            throw new InsufficientResourcesException();
        } else{
            entity.setAmount(remainingAmount);
            supplyRepository.save(entity);
        }
    }


}
