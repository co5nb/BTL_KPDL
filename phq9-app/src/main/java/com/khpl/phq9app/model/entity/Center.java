package com.khpl.phq9app.model.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "centers")
@AllArgsConstructor
@NoArgsConstructor
@Data
public class Center {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private float age;
    private float happiness_score;
    private float sex;
    private float depression_severity;
}
