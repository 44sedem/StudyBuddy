package com.myapp.data.repository

import com.myapp.domain.model.Course

interface CourseRepository {
    suspend fun getCoursesForStudent(studentId: String): List<Course>
    suspend fun createCourse(course: Course): Course
    suspend fun deleteCourse(courseId: String)
}
