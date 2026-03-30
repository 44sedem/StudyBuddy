package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class Subtask(
    val id: String,
    val taskId: String,
    val title: String,
    val estimatedMinutes: Int,
    val isCompleted: Boolean = false,
    val order: Int
)
