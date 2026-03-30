package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class Course(
    val id: String,
    val name: String,
    val code: String,
    val creditHours: Int,
    val professor: String = "",
    val colorHex: String = "#1A73E8"
)
