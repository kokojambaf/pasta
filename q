public async Task<IActionResult> OnPostAsync(IFormFile? file)
{
    if (!ModelState.IsValid)
        return Page();

    var filmFromDb = await _context.Films.FindAsync(Film.Id);
    if (filmFromDb == null)
        return NotFound();

    if (file?.Length > 0)
    {
        // 🔴 Проверка размера (до 3 МБ)
        if (file.Length > 3 * 1024 * 1024)
        {
            ModelState.AddModelError("", "Файл не должен превышать 3 МБ");
            return Page();
        }

        using var memoryStream = new MemoryStream();
        await file.CopyToAsync(memoryStream);

        filmFromDb.Photo = memoryStream.ToArray();
    }

    await _context.SaveChangesAsync();
    return RedirectToPage("Index");
}
