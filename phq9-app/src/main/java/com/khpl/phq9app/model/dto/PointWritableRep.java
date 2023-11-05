package com.khpl.phq9app.model.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class PointWritableRep {
    private String age;
    private String sex;
    private int happiness_score;
    private int depression_severity;
}
