package com.example.supply;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.math.BigInteger;

@Entity
@Setter
@Getter
@NoArgsConstructor
@Table(name = "resource")
public class ResourceEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String size;
    private BigInteger amount;
}
