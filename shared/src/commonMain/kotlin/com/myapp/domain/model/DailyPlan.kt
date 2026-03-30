package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class DailyPlan(
    val id: String,
    val studentId: String,
    val date: String,
    val energyRating: Int,
    val plannedTasks: List<PlannedTask>,
    val suggestedTechnique: StudyTechnique,
    val generatedAt: String
)

@Serializable
data class PlannedTask(
    val taskId: String,
    val startTime: String,
    val endTime: String,
    val priority: Int
)
