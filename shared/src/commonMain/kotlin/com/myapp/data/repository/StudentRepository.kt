package com.myapp.data.repository

import com.myapp.domain.model.Student
import com.myapp.domain.model.StudentProfile

interface StudentRepository {
    suspend fun getStudent(id: String): Student
    suspend fun updateProfile(studentId: String, profile: StudentProfile)
}
