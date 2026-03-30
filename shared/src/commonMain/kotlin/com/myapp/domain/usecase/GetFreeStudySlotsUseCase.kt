package com.myapp.domain.usecase

import com.myapp.data.repository.ScheduleRepository

class GetFreeStudySlotsUseCase(private val scheduleRepo: ScheduleRepository) {
    suspend operator fun invoke(studentId: String, date: String): List<Pair<String, String>> {
        return scheduleRepo.getFreeSlots(studentId, date)
    }
}
