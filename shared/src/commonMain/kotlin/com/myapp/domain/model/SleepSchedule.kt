package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class SleepSchedule(
    val bedtime: String,    // "23:00"
    val wakeTime: String    // "07:00"
)
