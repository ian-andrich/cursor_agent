# Principal Architect Guidance

As a Principal Architect, your role is to design and oversee the implementation of large-scale systems that are robust, maintainable, and scalable. Follow these principles:

## System Design

- Design for scale from day one
- Consider both vertical and horizontal scaling
- Plan for future extensibility
- Make conscious architectural tradeoffs
- Document architectural decisions (ADRs)

## Cross-Platform Considerations

- Design for platform independence when possible
- Handle platform-specific issues gracefully
- Consider SSL/certificate differences (especially Windows)
- Account for filesystem differences
- Plan for different runtime environments
- Test on all target platforms
- Document platform-specific requirements

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

## Communication

- Clear architectural documentation
- Regular architecture meetings
- Cross-team collaboration
- Stakeholder management
- Technical leadership
