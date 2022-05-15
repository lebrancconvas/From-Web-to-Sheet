import puppeteer from 'puppeteer';
import fs from 'fs';

const app = async() => {
	const browser = await puppeteer.launch({headless: false});
	const page = await browser.newPage();

	await page.goto('https://www.ddproperty.com/นโยบายความเป็นส่วนตัว');
	await page.waitForTimeout(2000);

	const selector = "#wrapper-inner > div.static-cms-page > section:nth-child(2) > div > div > section > article";

	await page.waitForSelector(selector);

	const element = await page.$(selector);

	const value = await page.evaluate(el => el.textContent, element);

	await page.close();
	await browser.close();

	fs.writeFileSync('./data/output.txt', value);
};

app();