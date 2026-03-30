package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class Task(
    val id: String,
    val title: String,
    val courseId: String,
    val deadline: String,
    val weightPercent: Float,   // e.g. 30.0 for 30% of final grade
    val gpaImpactScore: Float,  // computed: weightPercent * creditHours
    val estimatedMinutes: Int,
    val subtasks: List<Subtask> = emptyList(),
    val isCompleted: Boolean = false,
    val lastTouchedAt: String? = null
)
