package com.myapp.domain.usecase

import com.myapp.data.repository.AiRepository
import com.myapp.domain.model.DailyPlan

class GetDailyPlanUseCase(private val aiRepo: AiRepository) {
    suspend operator fun invoke(studentId: String, energyRating: Int): DailyPlan {
        return aiRepo.generateDailyPlan(studentId, energyRating)
    }
}
