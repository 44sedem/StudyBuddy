package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class Reward(
    val id: String,
    val studentId: String,
    val title: String,          // e.g. "30 min gaming"
    val triggerTaskId: String,  // unlocked after this task
    val isUnlocked: Boolean = false
)
