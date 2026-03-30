package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class StudentProfile(
    val studentId: String,
    val attentionSpanMinutes: Int,       // e.g. 25, 45, 90
    val dailyHoursCommitted: Float,      // e.g. 4.5
    val sleepSchedule: SleepSchedule,
    val timetableEntries: List<TimetableEntry> = emptyList(),
    val chronotype: Chronotype = Chronotype.UNKNOWN
)

enum class Chronotype { MORNING, EVENING, NEUTRAL, UNKNOWN }
