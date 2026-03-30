package com.myapp.data.repository

import com.myapp.domain.model.Task

interface TaskRepository {
    suspend fun getTasksForStudent(studentId: String): List<Task>
    suspend fun getIdleTasksNearDeadline(studentId: String, idleDays: Int): List<Task>
    suspend fun updateTask(task: Task)
    suspend fun createTask(task: Task): Task
}
