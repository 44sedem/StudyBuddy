package com.myapp.domain.usecase

import com.myapp.data.repository.TaskRepository
import com.myapp.domain.model.Task

class GetGpaWeightedTasksUseCase(private val repo: TaskRepository) {
    suspend operator fun invoke(studentId: String): List<Task> {
        return repo.getTasksForStudent(studentId)
            .sortedByDescending { it.gpaImpactScore }
    }
}
