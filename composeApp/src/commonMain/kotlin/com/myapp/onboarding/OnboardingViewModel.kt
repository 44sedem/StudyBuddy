package com.myapp.onboarding

import kotlinx.coroutines.flow.MutableStateFlow

class OnboardingViewModel {
    val currentStep = MutableStateFlow(0)
    val totalSteps = 5
    fun nextStep() { currentStep.value++ }
    fun previousStep() { if (currentStep.value > 0) currentStep.value-- }
}