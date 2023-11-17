package supply.system;

import org.springframework.data.repository.CrudRepository;

public interface SupplyRepository extends CrudRepository<ResourceEntity, Long> {
    ResourceEntity findBySize(String name);
}
