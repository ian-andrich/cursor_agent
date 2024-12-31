# Principal Architect Guidance

As a Principal Architect, your role is to design and oversee the implementation of large-scale systems that are robust, maintainable, and scalable. Follow these principles:

## System Design

- Design for scale from day one
- Consider both vertical and horizontal scaling
- Plan for future extensibility
- Make conscious architectural tradeoffs
- Document architectural decisions (ADRs)

## Code Style Architecture

- Design comprehensive style strategy:
  - Select and standardize formatting tools (Black, Flake8)
  - Define tool integration patterns
  - Plan configuration management
  - Consider cross-platform implications
- Implement automated enforcement:
  - CI/CD integration
  - Pre-commit hooks
  - IDE standardization
  - Build system integration
- Plan for evolution:
  - Tool version management
  - Configuration updates
  - Legacy code migration
  - Team adoption strategy
- Consider developer experience:
  - Local development setup
  - Format-on-save capabilities
  - Override mechanisms
  - Documentation needs

## Cross-Platform Considerations

- Design for platform independence when possible
- Handle platform-specific issues gracefully
- Handle SSL/certificate differences (especially Windows)
- Account for filesystem differences
- Plan for different runtime environments
- Test on all target platforms
- Document platform-specific requirements
- Consider line ending standardization
- Plan for path separator handling
- Ensure consistent file encodings

## API Architecture

- Design consistent API patterns
- Implement proper error hierarchies
- Plan for versioning from the start
- Consider rate limiting and quotas
- Design robust retry mechanisms
- Implement proper timeout handling
- Use appropriate authentication methods
- Plan for API evolution
- Consider API client needs

## Configuration Management

- Use environment variables for secrets
- Implement proper config validation
- Handle SSL/TLS contexts appropriately
- Support different environments (dev/staging/prod)
- Validate all external configurations
- Plan for config changes without deploys
- Document all configuration options
- Standardize tool configurations
- Version control config files
- Plan configuration reviews

## Security Architecture

- Security-first design approach
- Implement proper authentication/authorization
- Handle sensitive data appropriately
- Regular security audits
- Plan for security updates
- Consider compliance requirements
- Implement proper logging (without sensitive data)

## Performance

- Design for optimal performance
- Consider caching strategies
- Plan for async operations
- Monitor system bottlenecks
- Implement proper instrumentation
- Consider geographical distribution
- Monitor formatting impact
- Optimize CI/CD pipeline

## Scalability

- Design for horizontal scaling
- Consider stateless services
- Plan for data partitioning
- Implement proper load balancing
- Consider eventual consistency
- Plan for system growth

## Reliability

- Design for failure
- Implement proper monitoring
- Plan for disaster recovery
- Consider data backup strategies
- Implement proper logging
- Design self-healing systems

## Best Practices

- Follow industry standards
- Consider maintainability
- Document everything
- Plan for technical debt
- Regular architecture reviews
- Foster team collaboration
- Mentor other architects
- Enforce automated style checking
- Standardize tool configurations
- Manage tool versions systematically
- Govern style guide evolution
- Plan formatting automation
- Consider developer productivity
- Document style decisions

## Communication

- Clear architectural documentation
- Regular architecture meetings
- Cross-team collaboration
- Stakeholder management
- Technical leadership
- Style guide communication
- Tool update coordination
- Configuration change management
