package org.aki.javabackend.model.dto;

import java.util.Map;

public class AKIPredictionRequest {

    private String requestId;
    private Map<String, Object> features;
    private String modelVersion; // 可选，可为 null

    public AKIPredictionRequest() {}

    public AKIPredictionRequest(String requestId, Map<String, Object> features, String modelVersion) {
        this.requestId = requestId;
        this.features = features;
        this.modelVersion = modelVersion;
    }

    public String getRequestId() {
        return requestId;
    }

    public void setRequestId(String requestId) {
        this.requestId = requestId;
    }

    public Map<String, Object> getFeatures() {
        return features;
    }

    public void setFeatures(Map<String, Object> features) {
        this.features = features;
    }

    public String getModelVersion() {
        return modelVersion;
    }

    public void setModelVersion(String modelVersion) {
        this.modelVersion = modelVersion;
    }
}
