package com.khpl.phq9app.service.impl;

import com.khpl.phq9app.model.entity.Center;
import com.khpl.phq9app.model.entity.PointWritable;
import com.khpl.phq9app.repository.CenterRepository;
import com.khpl.phq9app.service.CenterService;
import com.khpl.phq9app.util.DataUtil;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CenterImpl implements CenterService {
    private final CenterRepository centerRepository;

    public CenterImpl(CenterRepository centerRepository) {
        this.centerRepository = centerRepository;
    }

    public List<Center> getAllCenters() {
        return centerRepository.findAll();
    }

    @Override
    public Center predict(List<Center> centers, PointWritable pointWritable) {
        pointWritable.setAge(minMaxScaling(pointWritable.getAge(), DataUtil.AGE_MIN, DataUtil.AGE_MAX));
        pointWritable.setHappiness_score(minMaxScaling(pointWritable.getHappiness_score(), DataUtil.HAPPINESS_SCORE_MIN, DataUtil.HAPPINESS_SCORE_MAX));
        pointWritable.setDepression_severity(minMaxScaling(pointWritable.getHappiness_score(), DataUtil.DEPRESSION_SEVERITY_MIN, DataUtil.DEPRESSION_SEVERITY_MAX));
        Center nearestCenter = centers.get(0);
        float minDistance = calculateDistance(centers.get(0), pointWritable);

        for (Center center : centers) {
            float distance = calculateDistance(center, pointWritable);
            if (distance < minDistance) {
                minDistance = distance;
                nearestCenter = center;
            }
        }
        return nearestCenter;
    }

    private Float calculateDistance(Center center,PointWritable pointWritable) {
        return (float) Math.sqrt(
                        Math.pow(center.getAge() - pointWritable.getAge(), 2) +
                        Math.pow(center.getHappiness_score() - pointWritable.getHappiness_score(), 2) +
//                        Math.pow(center.getTotal_period() - pointWritable.getTotal_period(), 2) +
                        Math.pow(center.getSex_female() - pointWritable.getSex_female(), 2) +
                        Math.pow(center.getSex_male() - pointWritable.getSex_male(), 2) +
                        Math.pow(center.getDepression_severity() - pointWritable.getDepression_severity(), 2)
                );
    }

    private float minMaxScaling(float value, float min, float max) {
        return (value - min) / (max - min);
    }
}
