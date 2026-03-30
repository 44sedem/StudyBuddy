package com.myapp.domain.usecase

import com.myapp.data.repository.AiRepository
import com.myapp.domain.model.Task

class DecomposeSyllabusUseCase(private val aiRepo: AiRepository) {
    suspend operator fun invoke(courseId: String, syllabusBytes: ByteArray): List<Task> {
        return aiRepo.parseSyllabusToTasks(courseId, syllabusBytes)
    }
}
