package com.myapp.data.repository

import com.myapp.domain.model.TimetableEntry

interface ScheduleRepository {
    suspend fun getTimetable(studentId: String): List<TimetableEntry>
    suspend fun getFreeSlots(studentId: String, date: String): List<Pair<String, String>>
}
