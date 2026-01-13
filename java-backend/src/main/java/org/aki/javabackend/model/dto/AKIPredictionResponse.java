package org.aki.javabackend.model.dto;

public class AKIPredictionResponse {

    private String requestId;
    private double akiRisk; // 风险值 0~1
    private String modelVersion;

    public AKIPredictionResponse() {}

    public AKIPredictionResponse(String requestId, double akiRisk, String modelVersion) {
        this.requestId = requestId;
        this.akiRisk = akiRisk;
        this.modelVersion = modelVersion;
    }

    public String getRequestId() {
        return requestId;
    }

    public void setRequestId(String requestId) {
        this.requestId = requestId;
    }

    public double getAkiRisk() {
        return akiRisk;
    }

    public void setAkiRisk(double akiRisk) {
        this.akiRisk = akiRisk;
    }

    public String getModelVersion() {
        return modelVersion;
    }

    public void setModelVersion(String modelVersion) {
        this.modelVersion = modelVersion;
    }
}
