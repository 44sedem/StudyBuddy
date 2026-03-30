package com.myapp.domain.model

import kotlinx.serialization.Serializable

@Serializable
data class Student(
    val id: String,
    val name: String,
    val email: String,
    val profile: StudentProfile,
    val courses: List<Course> = emptyList()
)
