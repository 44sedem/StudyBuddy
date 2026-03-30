package com.myapp.domain.usecase

import com.myapp.data.repository.AiRepository

class GetDeadlineCollisionsUseCase(private val aiRepo: AiRepository) {
    suspend operator fun invoke(studentId: String): List<String> {
        // Returns list of high-risk week labels e.g. ["Week 8", "Week 12"]
        return aiRepo.getDeadlineCollisionWeeks(studentId)
    }
}
