package com.khpl.phq9app.model.dto;

import jakarta.validation.constraints.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class PointWritableDTO {
    @Pattern(regexp = "^(?:[5-9]|[1-7][0-9]|80)$", message = "Tuổi không hợp lệ")
    private String age;


    @Pattern(regexp = "^[01]$", message = "Giới tính không hợp lệ")
    private String sex;

    @Pattern(regexp = "^[0-4]$", message = "Đáp án cho câu hỏi happiness score không hợp lệ")
    private String happiness_score;

    @Pattern(regexp = "^[0-3]$", message = "Đáp án cho câu hỏi phq1 không hợp lệ")
    private String phq1;

    @Pattern(regexp = "^[0-3]$", message = "Đáp án cho câu hỏi phq2 không hợp lệ")
    private String phq2;

    @Pattern(regexp = "^[0-3]$", message = "Đáp án cho câu hỏi phq3 không hợp lệ")
    private String phq3;

    @Pattern(regexp = "^[0-3]$", message = "Đáp án cho câu hỏi phq4 không hợp lệ")
    private String phq4;

    @Pattern(regexp = "^[0-3]$", message = "Đáp án cho câu hỏi phq5 không hợp lệ")
    private String phq5;

    @Pattern(regexp = "^[0-3]$", message = "Đáp án cho câu hỏi phq6 không hợp lệ")
    private String phq6;

    @Pattern(regexp = "^[0-3]$", message = "Đáp án cho câu hỏi phq7 không hợp lệ")
    private String phq7;

    @Pattern(regexp = "^[0-3]$", message = "Đáp án cho câu hỏi phq8 không hợp lệ")
    private String phq8;

    @Pattern(regexp = "^[0-3]$", message = "Đáp án cho câu hỏi phq9 không hợp lệ")
    private String phq9;
}
