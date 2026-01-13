package org.aki.javabackend.model.dto;

public class AKITaskStatusResponse {

    private String taskId;
    private String status;  // PENDING / RUNNING / DONE / FAILED
    private String message; // User可读信息

    public AKITaskStatusResponse() {}

    public AKITaskStatusResponse(String taskId, String status, String message) {
        this.taskId = taskId;
        this.status = status;
        this.message = message;
    }

    public String getTaskId() {
        return taskId;
    }

    public void setTaskId(String taskId) {
        this.taskId = taskId;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
