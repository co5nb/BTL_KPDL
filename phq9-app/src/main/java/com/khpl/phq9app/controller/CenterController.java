package com.khpl.phq9app.controller;

import com.khpl.phq9app.model.dto.PointWritableDTO;
import com.khpl.phq9app.model.dto.PointWritableRep;
import com.khpl.phq9app.model.entity.Center;
import com.khpl.phq9app.model.entity.PointWritable;
import com.khpl.phq9app.service.CenterService;
import com.khpl.phq9app.util.DataUtil;
import jakarta.validation.Valid;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.util.List;

@Controller
@RequestMapping("/phq9")
//http://localhost:8080/phq9
public class CenterController {
    private final CenterService centerService;
    public  CenterController(CenterService centerService){
        this.centerService = centerService;
    }

    @GetMapping("")
    public String formPredict(Model model) {
        model.addAttribute("pointWritableDTO" ,new PointWritableDTO());
        return "index";
    }

    @PostMapping("/predict")
    public String predict(RedirectAttributes redirectAttributes,Model model,
                          @ModelAttribute("pointWritableDTO") @Valid PointWritableDTO pointWritableDTO,
                          BindingResult bindingResult) {
        if(bindingResult.hasErrors()) {
            List<FieldError> errors = bindingResult.getFieldErrors();
            for (FieldError error : errors) {
                String field = error.getField();
                String errorMessage = error.getDefaultMessage();
                model.addAttribute(field + "Error", errorMessage);
            }
            model.addAttribute("haveError", "haveError");
            return "index";
        }

        List<Center> centers = centerService.getAllCenters();
        PointWritable pointWritable = getPointWritable(pointWritableDTO);
        PointWritableRep pointWritableRep = new PointWritableRep();
        pointWritableRep.setAge(pointWritableDTO.getAge());
        pointWritableRep.setGender(pointWritableDTO.getGender());
        pointWritableRep.setHappiness_score((int) pointWritable.getHappiness_score());
        pointWritableRep.setDepression_severity((int) pointWritable.getDepression_severity());

        String prediction = centerService.predict(centers, pointWritable).toString();

        redirectAttributes.addFlashAttribute("center", prediction);
        redirectAttributes.addFlashAttribute("pointWritableRep", pointWritableRep);
        redirectAttributes.addFlashAttribute("pointWritableDTO", pointWritableDTO);
        redirectAttributes.addFlashAttribute("result", "result");

        return "redirect:/phq9";
    }

    private PointWritable getPointWritable(PointWritableDTO pointWritableDTO) {
        PointWritable pointWritable = new PointWritable();

        float age = Float.parseFloat(pointWritableDTO.getAge());
        float happiness_score = Float.parseFloat(pointWritableDTO.getHappiness_score());
        float phq1 = Float.parseFloat(pointWritableDTO.getPhq1());
        float phq2 = Float.parseFloat(pointWritableDTO.getPhq2());
        float phq3 = Float.parseFloat(pointWritableDTO.getPhq3());
        float phq4 = Float.parseFloat(pointWritableDTO.getPhq4());
        float phq5 = Float.parseFloat(pointWritableDTO.getPhq5());
        float phq6 = Float.parseFloat(pointWritableDTO.getPhq6());
        float phq7 = Float.parseFloat(pointWritableDTO.getPhq7());
        float phq8 = Float.parseFloat(pointWritableDTO.getPhq8());
        float phq9 = Float.parseFloat(pointWritableDTO.getPhq9());
        float depression_severity = phq1 + phq2 + phq3 + phq4 + phq5 + phq6 + phq7 + phq8 + phq9;


        pointWritable.setAge(age);
        pointWritable.setHappiness_score(happiness_score);
        pointWritable.setDepression_severity(depression_severity);
        if(pointWritableDTO.getGender().equals("0")) {
            pointWritable.setSex_female(0);
            pointWritable.setSex_male(1);
        }else {
            pointWritable.setSex_female(1);
            pointWritable.setSex_male(0);
        }

        return pointWritable;
    }

}
