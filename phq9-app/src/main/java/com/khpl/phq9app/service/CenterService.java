package com.khpl.phq9app.service;

import com.khpl.phq9app.model.entity.Center;
import com.khpl.phq9app.model.entity.PointWritable;

import java.util.List;

public interface CenterService {
    public List<Center> getAllCenters();
    public Center predict(List<Center> centers, PointWritable pointWritable);
}
