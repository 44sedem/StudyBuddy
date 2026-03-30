package com.myapp.domain.usecase

import com.myapp.data.repository.TaskRepository
import com.myapp.domain.model.Task

class DetectProcrastinationUseCase(private val repo: TaskRepository) {
    suspend operator fun invoke(studentId: String): List<Task> {
        // Returns tasks not touched in 3+ days with approaching deadlines
        return repo.getIdleTasksNearDeadline(studentId, idleDays = 3)
    }
}
