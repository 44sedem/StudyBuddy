package com.myapp

import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application
import com.myapp.navigation.AppNavGraph
import com.myapp.ui.theme.AppTheme

fun main() = application {
    Window(onCloseRequest = ::exitApplication, title = "StudyBuddy") {
        AppTheme { AppNavGraph() }
    }
}
