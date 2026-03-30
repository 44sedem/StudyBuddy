package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class AccountabilityPair(
    val id: String,
    val studentAId: String,
    val studentBId: String,
    val createdAt: String,
    val isActive: Boolean = true
)
