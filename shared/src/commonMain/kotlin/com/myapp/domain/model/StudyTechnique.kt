package com.myapp.domain.model

enum class StudyTechnique(
    val label: String,
    val focusMinutes: Int,
    val breakMinutes: Int
) {
    POMODORO("Pomodoro", 25, 5),
    DEEP_WORK("Deep Work", 90, 20),
    FIVE_MINUTE("5-Minute Rule", 5, 0),
    SHORT_BURST("Short Burst", 15, 5)
}
