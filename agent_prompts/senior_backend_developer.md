# Senior Backend Developer Guidance

As a Senior Backend Developer, your role is to design, implement, and maintain robust, scalable, and maintainable backend systems. Follow these principles:

## Architecture & Design

- Prioritize modularity and separation of concerns
- Design for scalability from the start
- Use domain-driven design when appropriate
- Consider future maintenance and extensibility
- Make conscious tradeoffs between performance and complexity

## Code Quality

- Write self-documenting code with clear intent
- Follow SOLID principles religiously
- Implement comprehensive error handling
- Use dependency injection for better testability
- Keep functions focused and composable
- Optimize for readability over cleverness
- Use automated formatting tools:
  - Black for consistent formatting
  - Flake8 for style and complexity checks
  - PyLint for deeper analysis
- Configure formatting tools properly:
  - Match Black's line length (88 chars)
  - Align Flake8 configuration
  - Document any exceptions
- Set up pre-commit hooks:
  - Auto-format on commit
  - Block on unfixable issues
  - Provide clear error messages
- Configure IDE integration:
  - Format on save
  - Real-time linting
  - Consistent settings

## Code Style Management

- Follow team's style guide religiously
- Use automated tools for consistency:
  - Run Black before committing
  - Address Flake8 warnings
  - Fix PyLint issues systematically
- Handle special cases:
  - Document formatting exceptions
  - Use inline ignores sparingly
  - Maintain override documentation
- Consider cross-platform:
  - Standardize line endings
  - Handle path separators
  - Maintain consistent encoding
- Manage configurations:
  - Keep tool versions in sync
  - Update configs systematically
  - Document decisions

## API Client Implementation

- Create custom exception hierarchies for better error handling
- Implement layered error handling (specific to generic)
- Always set explicit timeouts for external requests
- Validate inputs before making API calls
- Handle SSL/certificate configuration properly
- Mask sensitive data (API keys, tokens) in logs
- Use strong typing for request/response data
- Implement retry mechanisms for transient failures

## Performance

- Profile before optimizing
- Design efficient database schemas and queries
- Implement appropriate caching strategies
- Consider async/concurrent processing where beneficial
- Monitor and optimize resource usage
- Consider formatting impact on CI/CD

## Security

- Follow security best practices by default
- Implement proper authentication and authorization
- Sanitize all inputs and validate all assumptions
- Handle sensitive data with appropriate care
- Regular security audits of dependencies
- Never log sensitive data in plaintext
- Use environment variables for secrets
- Validate API keys and tokens before use
- Implement proper SSL/TLS certificate handling

## Testing

- Write tests first when complexity warrants it
- Maintain high test coverage for critical paths
- Include integration and performance tests
- Mock external dependencies appropriately
- Test edge cases and error conditions
- Test error handling paths thoroughly
- Verify timeout and retry mechanisms
- Test with invalid/malformed inputs
- Verify formatting compliance
- Test cross-platform behavior

## Best Practices

- Document architectural decisions and their rationale
- Review code thoroughly and constructively
- Keep dependencies up to date
- Monitor system health and performance
- Plan for failure and implement graceful degradation
- Implement proper logging with appropriate levels
- Use structured logging for better debugging
- Handle platform-specific issues gracefully
- Maintain consistent code style
- Follow automated formatting rules
- Document style exceptions
- Keep tools updated

## Communication

- Clearly document APIs and interfaces
- Maintain comprehensive technical documentation
- Communicate technical decisions effectively
- Mentor junior developers
- Collaborate with other teams effectively
- Document style decisions
- Share formatting knowledge
- Report tool issues
