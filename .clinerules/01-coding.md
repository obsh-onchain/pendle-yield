# Coding Rules for Pendle Yield SDK

## Code Style & Formatting

1. **Use Ruff for all formatting and linting**
   - Run `pdm run format` after writing code
   - Run `pdm run lint` to check for issues
   - Line length: 88 characters (Black standard)
   - Use double quotes for strings
   - Follow PEP 8 with Ruff's selected rules (E, W, F, I, B, C4, UP)

2. **Import Organization**
   - Use absolute imports from `pendle_yield` package
   - Group imports: standard library, third-party, local
   - Let Ruff handle import sorting (isort rules)

## Type Hints & Type Safety

3. **Strict Type Hints Required**
   - All functions must have complete type annotations
   - Use `mypy --strict` compliance (configured in pyproject.toml)
   - Run `pdm run type-check` before committing
   - No `Any` types without explicit justification
   - Use `Optional[T]` or `T | None` for nullable types

4. **Pydantic Models**
   - All API responses and data structures use Pydantic models
   - Define models in `src/pendle_yield/models.py`
   - Use `ConfigDict` for model configuration
   - Validate data at boundaries (API responses, user inputs)

## Project Structure

5. **File Organization**
   - Source code in `src/pendle_yield/`
   - Tests in `tests/` with `test_` prefix
   - Examples in `examples/`
   - One class/concept per file when possible

6. **Module Responsibilities**
   - `client.py`: Main SDK client interface
   - `models.py`: Pydantic data models
   - `pendle.py`: Pendle-specific API interactions
   - `etherscan.py`: Etherscan API integration
   - `exceptions.py`: Custom exception classes

## Testing

7. **Test Requirements**
   - Write tests for all new functionality
   - Test files mirror source structure: `test_<module>.py`
   - Use pytest fixtures for common setup
   - Mark slow tests with `@pytest.mark.slow`
   - Mark integration tests with `@pytest.mark.integration`
   - Run `pdm run test` after completing task

## Error Handling

8. **Exception Management**
   - Define custom exceptions in `exceptions.py`
   - Inherit from appropriate base classes
   - Provide clear error messages
   - Handle API errors gracefully with retries where appropriate

## Dependencies

9. **Dependency Management**
   - Use PDM for all dependency management
   - Core dependencies: httpx, pydantic
   - Keep dependencies minimal
   - Pin major versions in pyproject.toml

## Documentation

10. **Code Documentation**
    - Use docstrings for all public functions/classes
    - Include type information in docstrings
    - Document exceptions that can be raised
    - Provide usage examples for complex functions

## Development Workflow

11. **Pre-commit Checks**
    - Run `pdm run check-all` before committing (runs lint, type-check, test)
    - Fix all linting errors
    - Ensure all tests pass
    - Verify type checking passes

12. **API Design**
    - Keep public API surface minimal and intuitive
    - Use async/await for I/O operations with httpx
    - Provide both sync and async interfaces where appropriate
    - Return Pydantic models for structured data

## Python Version

13. **Compatibility**
    - Target Python 3.11+ (as specified in pyproject.toml)
    - Use modern Python features (match/case, union types with |)
    - Avoid deprecated patterns

## Best Practices

14. **General Guidelines**
    - Keep functions small and focused
    - Avoid global state
    - Use constants for magic values
    - Prefer composition over inheritance
    - Make illegal states unrepresentable with types
