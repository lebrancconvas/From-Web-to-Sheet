import puppeteer from 'puppeteer';

const app = async() => {
	const browser = await puppeteer.launch({headless: true});
	const page = await browser.newPage();

	await page.goto('https://www.ddproperty.com/นโยบายความเป็นส่วนตัว');
	await page.waitForTimeout(2000);

	const selector = "article.article-detail";

	await page.waitForSelector(selector);

	const element = await page.$(selector);

	const value = await page.evaluate(el => el.textContent, element);

	await page.close();
	await browser.close();

	console.log(value);
};

app();