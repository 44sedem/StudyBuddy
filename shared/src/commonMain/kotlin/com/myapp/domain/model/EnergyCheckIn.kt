package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class EnergyCheckIn(
    val id: String,
    val studentId: String,
    val rating: Int,        // 1–5
    val date: String,
    val createdAt: String
)
