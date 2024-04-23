package com.starter.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    private static final String password = "randomBike";
    private static final String role = "api_tester_role";

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests((requests) -> requests
                .requestMatchers("/unsecured/*").permitAll()
                .requestMatchers("/secured/*").authenticated()
                .anyRequest().permitAll()
        ).httpBasic(Customizer.withDefaults()).csrf(AbstractHttpConfigurer::disable);
        return http.build();
    }

    @Bean
    public InMemoryUserDetailsManager userDetailsManager() {
        UserDetails user = User.withUsername("api_tester").password("{noop}" + password).roles(role).build();
        return new InMemoryUserDetailsManager(user);
    }
}
