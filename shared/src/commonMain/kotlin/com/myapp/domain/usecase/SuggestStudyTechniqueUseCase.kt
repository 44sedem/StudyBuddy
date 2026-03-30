package com.myapp.domain.usecase

import com.myapp.data.repository.AiRepository
import com.myapp.domain.model.StudyTechnique

class SuggestStudyTechniqueUseCase(private val aiRepo: AiRepository) {
    suspend operator fun invoke(studentId: String, energyRating: Int): StudyTechnique {
        return aiRepo.suggestTechnique(studentId, energyRating)
    }
}
