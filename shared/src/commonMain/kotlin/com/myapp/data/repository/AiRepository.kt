package com.myapp.data.repository

import com.myapp.domain.model.DailyPlan
import com.myapp.domain.model.StudyTechnique
import com.myapp.domain.model.Task

interface AiRepository {
    suspend fun generateDailyPlan(studentId: String, energyRating: Int): DailyPlan
    suspend fun suggestTechnique(studentId: String, energyRating: Int): StudyTechnique
    suspend fun parseSyllabusToTasks(courseId: String, syllabusBytes: ByteArray): List<Task>
    suspend fun getDeadlineCollisionWeeks(studentId: String): List<String>
    suspend fun decomposeTask(taskTitle: String, courseContext: String): List<String>
}
