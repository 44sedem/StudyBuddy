package com.myapp

import androidx.compose.ui.window.ComposeUIViewController
import com.myapp.navigation.AppNavGraph
import com.myapp.ui.theme.AppTheme

fun MainViewController() = ComposeUIViewController {
    AppTheme { AppNavGraph() }
}
