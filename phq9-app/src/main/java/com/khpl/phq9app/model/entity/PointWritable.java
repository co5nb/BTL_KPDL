package com.khpl.phq9app.model.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
public class PointWritable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private float age;
    private float happiness_score;
    private float total_period = 0;
    private float sex_female;
    private float sex_male;
    private float depression_severity;
}
