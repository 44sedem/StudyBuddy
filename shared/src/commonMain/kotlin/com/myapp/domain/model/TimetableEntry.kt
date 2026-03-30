package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class TimetableEntry(
    val id: String,
    val courseId: String,
    val type: EntryType,    // CLASS or LAB
    val dayOfWeek: Int,     // 1=Mon ... 7=Sun
    val startTime: String,  // "08:00"
    val endTime: String     // "10:00"
)

enum class EntryType { CLASS, LAB }
