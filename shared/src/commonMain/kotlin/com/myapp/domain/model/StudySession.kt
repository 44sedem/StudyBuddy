package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class StudySession(
    val id: String,
    val studentId: String,
    val taskId: String?,
    val technique: StudyTechnique,
    val durationMinutes: Int,
    val startedAt: String,
    val endedAt: String?
)
